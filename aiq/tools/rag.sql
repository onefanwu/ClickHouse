SET max_block_size = 128, max_threads = 64

SELECT count() FROM hackernews WHERE text != '' AND NOT ignore(embed(text))