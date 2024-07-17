from converter import converter
def main():
    convert = converter()
    print(convert.int2str(25))     # Output: "fifty five"
    print(convert.int2str(73))      # Output: "seventy three"
    print(convert.int2str(105))     # Output: "one hundred five"
    print(convert.int2str(1234))    # Output: "one thousand two hundred thirty four"
    print(convert.int2str(1000000)) # Output: "one million"
    
if __name__ == "__main__":
    main()
