class Solution {
    /**
     * @param {string[]} strs
     * @return {string[][]}
     */
    groupAnagrams(strs) {
        let map = new Map()

        for(let word of strs) {
          let sortedWord = word.split("").sort().join("")

          if(map.has(sortedWord)) {
            map.get(sortedWord).push(word)
          } else {
            map.set(sortedWord, [word])
          }

        }
        return Array.from(map.values())
    }
}
