select COUNT(t.Id) c, t.status, t.Request_at Day from
    (SELECT Id, Request_at, Status, Client.Banned b1, Driver.Banned b2 FROM Trips
        LEFT JOIN Users Client
        ON Trips.Client_Id = Client.User_Id
        LEFT JOIN Users Driver
        ON Trips.Driver_Id = Driver.User_Id
        having b1="No" and b2="No"
    ) t GROUP BY t.status, Day as tmp;


select * from tmp
    left join
        (select * from tmp where status='completed') tmp2 on tmp.Day = tmp2.Day
    left join
        (select * from   tmp where status='cancelled_by_driver') tmp3 on tmp.Day = tmp3.Day
    left join (select * from tmp where status='cancelled_by_client') tmp4 on tmp.Day = tmp4.Day
;
