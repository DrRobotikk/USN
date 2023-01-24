--To obtain information about the constraints for a given table, try this SQL statement: 
SELECT * FROM information_schema.table_constraints 
WHERE information_schema.table_constraints.table_name='actor'; 

--To obtain the constraints for the table customer try this SQL statement: 
SELECT * FROM information_schema.table_constraints 
WHERE information_schema.table_constraints.table_name='customer'; 