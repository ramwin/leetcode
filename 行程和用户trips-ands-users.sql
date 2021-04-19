select COUNT(t.Id) c, t.status, t.Request_at Day from
    (SELECT Id, Request_at, Status, Client.Banned b1, Driver.Banned b2 FROM Trips
        LEFT JOIN Users Client
        ON Trips.Client_Id = Client.User_Id
        LEFT JOIN Users Driver
        ON Trips.Driver_Id = Driver.User_Id
        having b1="No" and b2="No"
    ) t GROUP BY t.status, Day as tmp;


    select 
        tmp.day day,
        completed.c completed,
        cancelled_by_c.c cancelled_by_client,
        cancelled_by_d.c cancelled_by_driver,
        completed.c/(coalesce(completed.c, 0) + coalesce(cancelled_by_c.c, 0) + coalesce(cancelled_by_d.c, 0)) ratio
    from tmp
    left join tmp completed
        on tmp.day=completed.day and completed.status='completed'
    left join tmp cancelled_by_c
        on tmp.day=cancelled_by_c.day and cancelled_by_c.status='cancelled_by_client'
    left join tmp cancelled_by_d
        on tmp.day=cancelled_by_d.day and cancelled_by_d.status='cancelled_by_driver';
