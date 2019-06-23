const strs = ['t', 's', 'e', 'b']

let best = strs.reduceRight( (a, v) => a + v )

console.log(best);
