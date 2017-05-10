select a.Id from Weather a left join Weather b ON TO_DAYS(a.Date)-1 = TO_DAYS(b.Date) where a.Temperature > b.Temperature
