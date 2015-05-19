import chunker as c
import xml_writer as x

the_dir = '/Users/hah661/Documents/Northwestern/MyPHD/social_policy_course/SocPol_Video/transcript_txts/'

a_lambda = lambda x: "poor" in c.words_inside_chunk(x) and len(c.words_inside_chunk(x)) > 5

mychunks = c.chunk(the_dir + 'all_out.csv', 120, a_lambda)


x.write_chunks(mychunks, "test", the_dir+"testfile")



