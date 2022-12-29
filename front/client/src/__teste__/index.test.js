const index = require('../page/sum');

test('adds 1+ 2 to equals ', ()=>{
    expect(index(1,2)).toBe(3);
});