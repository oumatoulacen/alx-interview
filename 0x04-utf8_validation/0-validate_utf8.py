#!/usr/bin/python3
'''determines if a given data set represents a valid UTF-8 encoding.'''


def validUTF8(data):
    '''determines if a given data set represents a valid UTF-8 encoding.'''
    
    def is_start_of_char(byte):
        '''check if a given byte is a valid start of a UTF-8 character'''
        return (byte & 0b10000000) == 0b00000000
    
    def is_valid_following_bytes(num_following):
        '''check if the number of following bytes is valid'''
        return 1 <= num_following <= 3
    
    i = 0
    while i < len(data):
        '''Get the number of following bytes based on the first byte'''
        leading_bits = bin(data[i])[2:].zfill(8)
        num_following_bytes = leading_bits.find('0', 1)
        
        if not is_valid_following_bytes(num_following_bytes):
            '''Check if the number of following bytes is valid'''
            return False
        
        for j in range(1, num_following_bytes + 1):
            '''Check if the current byte is a valid continuation byte'''
            if i + j >= len(data) or not is_start_of_char(data[i + j]):
                return False
        
        # Move to the next character
        i += num_following_bytes + 1
    
    return True
