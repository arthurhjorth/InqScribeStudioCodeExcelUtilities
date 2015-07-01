## this class takes a list of entries and a list of tags, and adds them to each entry

def copy_entries(entries):
	return [dict(entry) for entry in entries]

def apply_tags(entries, tags, tag_name):
	if len(entries) != len(tags):
		raise "hep"
	entries_copy = copy_entries(entries)
	for n in range(len(entries_copy)):
		the_entry = entries_copy[n]
		entries_copy[n][tag_name] = tags[n]
	return entries_copy

def remove_tag(entries, tag_name):
	entries_copy = copy_entries(entries)
	for entry in entries_copy:
		del entry[tag_name]
	return entries_copy