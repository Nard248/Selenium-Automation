SELECT a.PartnerUserId,
       CASE WHEN SUM(a.GGR * 0.22) >= 100000 THEN 100000 ELSE SUM(a.GGR * 0.22) END AS Cashback
FROM (
    SELECT u.PartnerUserId,
           o.GameID,
           SUM(o.OrderAmount - o.WinAmount) GGR
        FROM
            casino.orders AS o
        INNER JOIN
            C_Game AS g
                ON g.GameID=o.GameID
        INNER JOIN
            VIEW_PlatformPartnerUsers_TotogamingAm u
                ON u.UserID = o.UserID
        INNER JOIN
            C_GameCategory gc
                ON g.GameCategoryID = gc.GameCategoryID
        INNER JOIN
                C_GameProvider gp on g.GameProviderID = gp.GameProviderID
        WHERE
            o.CalculatiONDate  < '2023-03-16 20:00'
            AND o.CalculationDate >= '2023-03-15 20:00'
            AND o.OperationTypeID IN (
                3, 299
            )
            AND o.OrderStateID NOT IN (
                1, 4, 7
            )
            AND g.GameProviderID = 20
            AND (gc.GameCategoryName LIKE 'Slots' OR (gp.GameProviderName LIKE '%EGT%' AND g.Name_en LIKE '%Burning Keno Plus%' OR gp.GameProviderName LIKE '%EGT%'
                     AND g.Name_en LIKE '%European Roulette%'))
        GROUP BY
            o.GameID, u.PartnerUserId
        HAVING SUM(o.OrderAmount - o.WinAmount) > 0) a
group by a.PartnerUserId
HAVING SUM(a.GGR * 0.22) >= 1000
