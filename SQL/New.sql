SELECT bf.PartnerUserId,
       MAX(bf.LastOrderDate) AS LastOrderDate
FROM (
--Sport
SELECT u.PartnerUserId,
    MAX(o.CalculationDate_DT) AS LastOrderDate
FROM VIEW_sport_OrdersBetsStakes_TotogamingAm AS o
    INNER JOIN VIEW_sport_PartnerUser_TotogamingAm AS u ON u.UserID = o.UserID
    FULL OUTER JOIN VIEW_PlatformPartnerUsers_TotogamingAm cu ON cu.PartnerUserId = u.PartnerUserId
WHERE o.OrderStateID IN (2,3,5,6,8,9,10)
  AND o.CalculationDate_DT >= '2022-01-01'
  AND o.CalculationDate_DT <= '2022-09-30'
  AND u.isDeleted NOT IN (1)
  AND o.DeviceTypeID NOT IN (1)
GROUP BY u.PartnerUserId

UNION ALL

--Casino
SELECT u.PartnerUserId,
       MAX(o.CalculationDate_DT) AS LastOrderDate
FROM casino.orders AS o
    INNER JOIN VIEW_PlatformPartnerUsers_TotogamingAm u on u.UserID = o.UserID
    INNER JOIN C_Game g on o.GameID = g.GameID
WHERE o.CalculationDate_DT >= '2022-01-01'
  AND o.CalculationDate_DT <= '2022-09-30'
  AND o.OperationTypeID IN (3,299)
  AND g.GameProviderID <>3
  AND o.OrderStateID    IN (2,3,5,6,8,9,10) AND CASE WHEN g.GameProviderID IN (48, 10) THEN o.TypeId ELSE 0 END IN (0, 1, 5, 8, 18, 33)
GROUP BY u.PartnerUserId) bf
WHERE NOT EXISTS(
    SELECT 1
        FROM (SELECT u.PartnerUserId
             FROM VIEW_sport_OrdersBetsStakes_TotogamingAm AS o
             INNER JOIN VIEW_sport_PartnerUser_TotogamingAm AS u ON u.UserID = o.UserID
             --     FULL OUTER JOIN VIEW_PlatformPartnerUsers_TotogamingAm cu ON cu.PartnerUserId = u.PartnerUserId
             WHERE o.OrderStateID IN (2,3,5,6,8,9,10)
               AND u.PartnerUserId = bf.PartnerUserId
               AND o.CalculationDate_DT > '2022-09-30'
               AND u.isDeleted NOT IN (1)
               AND o.DeviceTypeID NOT IN (1)
             GROUP BY u.PartnerUserId

             UNION ALL

             --Casino
             SELECT u.PartnerUserId
             FROM casino.orders AS o
                 INNER JOIN VIEW_PlatformPartnerUsers_TotogamingAm u on u.UserID = o.UserID
                 INNER JOIN C_Game g on o.GameID = g.GameID
             WHERE o.CalculationDate_DT > '2022-09-30'
               AND u.PartnerUserId = bf.PartnerUserId
               AND o.OperationTypeID IN (3,299)
               AND g.GameProviderID <>3
               AND o.OrderStateID    IN (2,3,5,6,8,9,10) AND CASE WHEN g.GameProviderID IN (48, 10) THEN o.TypeId ELSE 0 END IN (0, 1, 5, 8, 18, 33)
             GROUP BY u.PartnerUserId) abs )
GROUP BY bf.PartnerUserId