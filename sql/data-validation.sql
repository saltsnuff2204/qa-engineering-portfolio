-- Restaurant Menu Manager QA validation queries
-- Run only against a disposable local test database.

-- 1. Review the newest records created by UI or API tests.
SELECT id, name, price, category, type, vegetarian, has_ice
FROM menu_items
ORDER BY id DESC
LIMIT 20;

-- 2. Verify mandatory-field and positive-price constraints.
SELECT *
FROM menu_items
WHERE name IS NULL
   OR BTRIM(name) = ''
   OR price <= 0
   OR category IS NULL
   OR type IS NULL;

-- 3. Find invalid dish/drink category combinations.
SELECT *
FROM menu_items
WHERE (type = 'DRINK' AND category <> 'DRINK')
   OR (type = 'DISH' AND category = 'DRINK');

-- 4. Find inconsistent type-specific attributes.
SELECT *
FROM menu_items
WHERE (type = 'DISH' AND (vegetarian IS NULL OR has_ice IS NOT NULL))
   OR (type = 'DRINK' AND (has_ice IS NULL OR vegetarian IS NOT NULL));

-- 5. Check category and type distributions after seeded tests.
SELECT category, type, COUNT(*) AS item_count
FROM menu_items
GROUP BY category, type
ORDER BY category, type;

-- 6. Identify duplicate-looking names for exploratory review.
SELECT LOWER(BTRIM(name)) AS normalized_name, COUNT(*) AS duplicate_count
FROM menu_items
GROUP BY LOWER(BTRIM(name))
HAVING COUNT(*) > 1
ORDER BY duplicate_count DESC, normalized_name;

-- 7. Verify one item by ID after an API create response.
-- Replace :created_id in the SQL client with the returned ID.
SELECT id, name, price, category, type, vegetarian, has_ice
FROM menu_items
WHERE id = :created_id;

