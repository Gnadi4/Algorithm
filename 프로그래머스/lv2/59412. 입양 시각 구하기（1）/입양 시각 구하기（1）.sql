-- 코드를 입력하세요
SELECT hour(DATETIME), count(hour(DATETIME))
FROM ANIMAL_OUTS
WHERE hour(DATETIME) between 9 and 20
GROUP BY hour(DATETIME)
order by hour(DATETIME)