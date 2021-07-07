from random import seed
from posproc.key import Random_Key_Generator

size = 1000
seed = 99
algorithm = 'original'
copy_method = 'exact'
fraction_of_bits_for_qber_estm = 0.1
noise = 1

ak = Random_Key_Generator(size,seed)
bk = ak.copy(noise,copy_method)


"""
TEST1  
---------------------
{seed = 100, size = 1000, algorithm = 'original',
copy_method = 'exact', fraction_of_bits_for_qber_estm = 0.1}

Before Cascade:
    Correct_Key_Initial = 011011100011001010000111011110000100000011000111110110100000001011101010000010001101011101001001001011001000101100101100100110111110101001110111001001000101110010000101010100100000000001010111110110100111101100010010101110100110110110110100110010000101111111000001110000011101111110010111000011011001010001001110000100001101110001010101000011111011111101011111000001000011101011111000010100000110101010010111001110101001010010010001100100100000110110110100000001011101010000010001101011101000001001101110001010110101001001000101010011100111111100011100000000011110110001100111001001011001000101100101100100110111110100010100110010110110011011100001000101001011010000001001000001101000010011010000010001111001101100100000010111111000111101000000011011011110101101100100111101100010010100111001110100000101100001110111110001011001010011100011000110000100011101001101101101101001100100001011111110000011100000111011111101010101111101110010100100011010101111110011000101110110001111110111111010111110000010000111010111110000101000001101010100101110011101010010100100100001010011011010110011000110100001011001001001010111111101110000010011011100010101101010010010001010100111001111111000111000000000111101100011001100100110111011110010101110010000011111011100001000101011000011010111000010001010010110100000010010000011010000100110100000100011110011011001000000110001100100101101110110111110111100111101001101100001011010001001110011101000001011000011101111100010110010100111000110001100001000
    Noisy_Key_Initial = 1101111111000001110010011011010110011110111100000101001001100101100011000001111111011001110010010111011101111001100101100100001011110111100001101001011110000100001101101000101111001010111111101000101011111000000111111011111000001010001100001111101101101111001100001101000010010011101000111010001101111111001001011000011001111010100001011000011101110110000101001110100010011000101100101101111010001111010010000110011111000010000001101110011010100111001100111001001011000110000011101111010100101111011001101011101110011101111111000111101111001001010111111110100011111000101011110000001000101111000000111011110000111010011101101111111101010111110010111110000101011110101110000110000111010110000001011010100000111000010001010110010000110011010101001110010011111110001101001001101111111100000100000110001010010111100011000101011011100001000101010100011100010000111100111011110000111010100111010010111001110011101101111110011011000011011011100101100101001010110100101100001111001100011100100001010111010001

QBER = 0.53

After Cascade:
    Correct_Key_Alice = 011011000110010100001110111000010000001100011111001101110010010001011100100001101010010000000000101011111010010111000010101010001001110001001101110001011100011110011010100000101111010000000111001000001000110101111001000010110010010110010110010110111110100101001100101111001011111100011111000000011011011110101101101011101100001010111010110110101100011001000001111110000100000110111111010101011111011001010010001100101111001001011101100011111101111101011111000001000011010111110000101000001010010010111011101010010010010000010011011010110011000110000010110010100100111111101100000011011100001011010110010001001001100111111100011100000000111011000110011010011011011100101011100000011111011100001000101110001101110010001010010110100000100000011010000100111000001000111100101100000001100100001011011101101111101111001111010011110000110100010011100111010000101100011101111100011100010011100011001100001000
    Reconciled_Key_Bob = 011011000110010100001110111000010000001100011111001101110010010001011100100001101010010000000000101011111010010111000010101010001001110001001101110001011100011110011010100000101111010000000111001000001000110101111001000010110010010110010110010110111110100101001100101111001011111100011111000000011011011110101101101011101100001010111010110110101100011001000001111110000100000110111111010101011111011001010010001100101111001001011101100011111101111101011111000001000011010111110000101000001010010010111011101010010010010000010011011010110011000110000010110010100100111111101100000011011100001011010110010001001001100111111100011100000000111011000110011010011011011100101011100000011111011100001000101110001101110010001010010110100000100000011010000100111000001000111100101100000001100100001011011101101111101111001111010011110000110100010011100111010000101100011101111100011100010011100011001100001000

Time = 0.03855640000000002 second(s) 
"""
