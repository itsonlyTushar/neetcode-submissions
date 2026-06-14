class Solution {
    /**
     * @param {string} s
     * @return {boolean}
     */
    isPalindrome(s) {
      let newStr = s.toLowerCase().replace(/[^a-z0-9]/gi, "").split("")
        let left = 0
        let right = newStr.length - 1

        while(left < right) {
            if(newStr[left] !== newStr[right]) {
                return false
            }
            left++
            right--
        }
    return true
    }
}
