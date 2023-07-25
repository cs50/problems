
-- The Lost Letter
-- My first query was to take a look at the packages sent out from 900 Somerville Avenue;
SELECT *
FROM "packages"
WHERE "from_address_id" IN
(
    SELECT "id"
    FROM "addresses"
    WHERE "address" = "900 Somerville Avenue"
);

-- output;
-- 384|Congratulatory letter|432|854
-- 2437|String|432|484
-- 3529|Letter opener|432|585
-- 5436|Whiteboard|432|4984

-- The first of these is the Congratulatory letter we're looking for;
-- now we want to look at the location it got sent to.
SELECT *
FROM "addresses"
WHERE "id" = 854;

-- output;
-- 854|2 Finnigan Street|Residential

-- If this is the location it actually ended up at, we're all done! Let's see if it actually ended up there using a JOIN;

SELECT "a"."address", "s"."action"
FROM "scans" AS "s"
JOIN "addresses" AS "a"
ON "s"."address_id" = "a"."id"
WHERE "package_id" = 384;

-- output;
-- 900 Somerville Avenue|Pick
-- 2 Finnigan Street|Drop

-- Then we're done!


-- The Devious Delivery
-- This took some trial and error, but it turns out the most germane piece of information is that there's literally no 'from' address;
SELECT *
FROM "packages"
WHERE "from_address_id" IS NULL;

-- output;
-- 5098|Duck debugger||50

-- Good stuff; only one package fits this description, and it aligns with the quack wink-and-nod the mysterious fellow gave. Same thing as before;
SELECT *
FROM "addresses"
WHERE "id" = 5098;

-- output;
-- 5098|1491 Wharf Street|Business
-- This is the intended destination; let's see where it ended up.

SELECT "a"."address", "s"."action"
FROM "scans" AS "s"
JOIN "addresses" AS "a"
ON "s"."address_id" = "a"."id"
WHERE "package_id" = 5098;

-- output;
-- 123 Sesame Street|Pick
-- 7 Humboldt Place|Drop

-- It's gone elsewhere! Namely,

SELECT "type"
FROM "addresses"
WHERE "address" = "7 Humboldt Place";

-- output;
-- Police Station

-- Oh dear..


-- The Forgotten Gift
-- First, we check the outgoing packages from 109 Tileston Street, in much the same way we did for the Lost Letter;
SELECT *
FROM "packages"
WHERE "from_address_id" IN
(
    SELECT "id"
    FROM "addresses"
    WHERE "address" = "109 Tileston Street"
);

-- output;
-- 9523|Flowers|9873|4983

-- So let's see if it ended up there;
SELECT "a"."address", "s"."action", "s"."driver_id"
FROM "scans" AS "s"
JOIN "addresses" AS "a"
ON "s"."address_id" = "a"."id"
WHERE "package_id" = 9523;

-- output;
-- 109 Tileston Street|Pick|11
-- 950 Brannon Harris Way|Drop|11
-- 950 Brannon Harris Way|Pick|17

-- Ah; it got delivered to the wrong place, and is now in the hands of the driver, presumably for the right place! Let's look up the name of the driver who did the last pickup;

SELECT "name"
FROM "drivers"
WHERE "id" = 17;

-- output;
-- Mikel

-- So Mikel's got it!


-- The above results as single queries;

-- The lost letter; get where it ended up at, what kind of place it ended up at, and what it consists of;
-- condition on it being sent from 900 Somerville Avenue, being a congraulatory item of some kind, and being a dropoff
SELECT "a"."address", "a"."type", "p"."contents"
FROM "scans" AS "s"
JOIN "addresses" AS "a"
ON "s"."address_id" = "a"."id"
JOIN "packages" AS "p"
ON "s"."package_id" = "p"."id"
WHERE "p"."from_address_id" IN (
    SELECT "id"
    FROM "addresses"
    WHERE "address" = "900 Somerville Avenue"
)
AND LOWER("p"."contents") LIKE LOWER("%congratulat%")
AND "s"."action" = "Drop";

-- The devious delivery; get where it ended up at, what kind of place it ended up at, and what it consists of;
-- condition on it having no "from" address and being a dropoff
SELECT "a"."address", "a"."type", "p"."contents"
FROM "scans" AS "s"
JOIN "addresses" AS "a"
ON "s"."address_id" = "a"."id"
JOIN "packages" AS "p"
ON "s"."package_id" = "p"."id"
WHERE "p"."from_address_id" IS NULL
AND "s"."action" = "Drop";

-- The forgotten gift; get the name of the driver
-- condition for the driver of the last scan done for a package from 109 Tileston Street
SELECT "d"."name", "p"."contents"
FROM "scans" AS "s"
JOIN "addresses" AS "a"
ON "s"."address_id" = "a"."id"
JOIN "packages" AS "p"
ON "s"."package_id" = "p"."id"
JOIN "drivers" AS "d"
ON "s"."driver_id" = "d"."id"
WHERE "p"."from_address_id" IN (
    SELECT "id"
    FROM "addresses"
    WHERE "address" = "109 Tileston Street"
)
ORDER BY "s"."timestamp" DESC
LIMIT 1;
