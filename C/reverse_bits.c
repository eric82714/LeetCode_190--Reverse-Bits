uint32_t reverseBits(uint32_t n) {
    uint32_t mod = 0, result = 0, counter = 0;
        
    while(n || counter < 32){
        mod = n % 2;
        n /= 2;
        result = (result * 2) + mod;
        counter ++;
    }    
    
    return result;
}
