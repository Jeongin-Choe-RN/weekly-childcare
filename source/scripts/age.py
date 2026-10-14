#!/usr/bin/env python3
# SPDX-License-Identifier: PolyForm-Noncommercial-1.0.0
# Required Notice: Copyright 2026 Jeongin Choe (최정인)
# License: https://polyformproject.org/licenses/noncommercial/1.0.0
"""Calculate completed calendar months, not days divided by 30."""
import argparse
import calendar
import json
from datetime import date, datetime
from zoneinfo import ZoneInfo


def add_months(birth, months):
    index = birth.year * 12 + birth.month - 1 + months
    year, month0 = divmod(index, 12)
    month = month0 + 1
    return date(year, month, min(birth.day, calendar.monthrange(year, month)[1]))


def age_at(birth, on):
    if on < birth:
        raise ValueError("Reference date precedes birth date")
    months = (on.year - birth.year) * 12 + on.month - birth.month
    if add_months(birth, months) > on:
        months -= 1
    return months, (on - add_months(birth, months)).days


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--birth", required=True, type=date.fromisoformat)
    parser.add_argument("--as-of", type=date.fromisoformat)
    parser.add_argument("--due", type=date.fromisoformat, help="Reported due date, for a preterm child only")
    args = parser.parse_args()
    on = args.as_of or datetime.now(ZoneInfo("Asia/Seoul")).date()
    try:
        months, days = age_at(args.birth, on)
    except ValueError as error:
        parser.error(str(error))
    corrected = None
    if args.due:
        if args.due <= args.birth:
            parser.error("For preterm correction, due date must be after birth date")
        if on < args.due:
            corrected = {"days_before_due_date": (args.due - on).days}
        else:
            corrected_months, corrected_days = age_at(args.due, on)
            corrected = {"completed_months": corrected_months, "additional_days": corrected_days}
    print(json.dumps({
        "birth_date": str(args.birth), "as_of": str(on), "timezone": "Asia/Seoul",
        "completed_months": months, "additional_days": days,
        "corrected_age_from_reported_due_date": corrected,
        "correction_note": "Developmental reference only, usually during the first two years; follow clinician advice. Not a vaccine or screening schedule.",
        "upcoming_age_dates": {
            str(m): str(add_months(args.birth, m))
            for m in (2, 4, 6, 9, 12, 15, 18, 24, 30, 36, 42, 48, 54, 60, 66, 72)
            if add_months(args.birth, m) >= on
        },
        "note": "Upcoming dates are calendar-age dates, not individualized examination deadlines."
    }, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
