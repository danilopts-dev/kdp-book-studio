"""Datas de calendário/planner: grade do mês, feriados (EUA) e datas judaicas (pyluach).

Feriados vêm de bibliotecas, nunca de memória do modelo.
"""
from __future__ import annotations

import calendar as pycal
from datetime import date

WEEKDAYS = {"sunday": pycal.SUNDAY, "monday": pycal.MONDAY}


def month_grid(year: int, month: int, week_start: str = "sunday") -> list[list[int]]:
    """Semanas do mês; 0 = dia fora do mês."""
    return pycal.Calendar(WEEKDAYS[week_start]).monthdayscalendar(year, month)


def us_holidays(year: int) -> dict[str, str]:
    import holidays
    return {d.isoformat(): name for d, name in sorted(holidays.US(years=year).items())}


def jewish_days(year: int, israel: bool = False) -> dict[str, dict]:
    """Por data civil: data hebraica, festividade e parashá de Shabat."""
    from pyluach import dates, parshios

    out: dict[str, dict] = {}
    d = date(year, 1, 1)
    end = date(year, 12, 31)
    while d <= end:
        h = dates.HebrewDate.from_pydate(d)
        info = {"hebrew": h.hebrew_date_string(), "hebrew_en": f"{h.day} {h.month_name()}"}
        fest = h.festival(israel=israel, hebrew=False)
        if fest:
            info["festival"] = fest
        fast = h.fast_day(hebrew=False)
        if fast:
            info["fast"] = fast
        if d.weekday() == 5:
            p = parshios.getparsha_string(h, israel=israel)
            if p:
                info["parsha"] = p
        out[d.isoformat()] = info
        d = date.fromordinal(d.toordinal() + 1)
    return out


def build_year(year: int, week_start: str = "sunday", us: bool = True, jewish: bool = False,
               months: list[int] | None = None) -> dict:
    hol = us_holidays(year) if us else {}
    jew = jewish_days(year) if jewish else {}
    out = []
    for m in months or range(1, 13):
        days = {}
        for wk in month_grid(year, m, week_start):
            for dnum in wk:
                if not dnum:
                    continue
                iso = date(year, m, dnum).isoformat()
                notes = []
                if iso in hol:
                    notes.append(hol[iso])
                j = jew.get(iso, {})
                for k in ("festival", "fast"):
                    if k in j:
                        notes.append(j[k])
                if "parsha" in j:
                    notes.append(f"Parashat {j['parsha']}")
                entry = {}
                if notes:
                    entry["notes"] = notes
                if j:
                    entry["hebrew"] = j["hebrew_en"]
                if entry:
                    days[str(dnum)] = entry
        out.append({
            "month": m,
            "name": pycal.month_name[m],
            "weeks": month_grid(year, m, week_start),
            "days": days,
        })
    return {"year": year, "week_start": week_start, "months": out}
