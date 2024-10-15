
create table full_table as
select
	sequence_table.sequence_id AS sequence_number, scientific_name, common_name, location, seq AS sequence, sequence_table.length, accession, score, hit_table.length AS hit_length
from
	sample_table, sequence_table, hit_table
where
	sequence_table.sample_id=sample_table.sample_id
	and
	hit_table.sequence_id=sequence_table.sequence_id;
