DROP TABLE IF EXISTS #EGT_PLAYED
SELECT u.PartnerUserId
INTO #EGT_PLAYED
FROM VIEW_PlatformPartnerUsers_TotogamingAm u
WHERE EXISTS(
    SELECT 1
    FROM casino.orders o
        INNER JOIN C_GameProvider cg ON o.GameProviderId = cg.GameProviderID
    WHERE o.CalculationDate >= '2023-03-10 16:30'
      AND o.CalculationDate <  '2023-03-10 20:40'
      AND cg.GameProviderName LIKE '%EGT%'
      AND u.UserID = o.UserID)

DROP TABLE IF EXISTS #EGT_PLAYED_AFTER
SELECT u.PartnerUserId
INTO #EGT_PLAYED_AFTER
FROM VIEW_PlatformPartnerUsers_TotogamingAm u
WHERE EXISTS(
    SELECT 1
    FROM casino.orders o
        INNER JOIN C_GameProvider cg ON o.GameProviderId = cg.GameProviderID
    WHERE o.CalculationDate >= '2023-03-10 21:00'
      AND cg.GameProviderName LIKE '%EGT%'
      AND u.UserID = o.UserID)


SELECT u.PartnerUserId, egt.PartnerUserId, egta.PartnerUserId
FROM VIEW_PlatformPartnerUsers_TotogamingAm u
    LEFT JOIN #EGT_PLAYED egt ON egt.PartnerUserId = u.PartnerUserId
    LEFT JOIN #EGT_PLAYED_AFTER egta on egt.PartnerUserId = egta.PartnerUserId
WHERE NOT EXISTS(
    SELECT 1
    FROM casino.orders o
        INNER JOIN C_GameProvider cg ON o.GameProviderId = cg.GameProviderID
    WHERE o.CalculationDate >= '2023-03-06 20:00'
      AND o.CalculationDate <  '2023-03-10 16:00'
      AND cg.GameProviderName LIKE '%EGT%'
      AND u.UserID = o.UserID)
