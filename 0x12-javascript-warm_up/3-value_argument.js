#!/usr/bin/node

const args = process.argv.slice(2);
let count = 0;

args.forEach(arg => {
  count++;
});

if (!count) {
  console.log('No argument');
} else if (count === 1) {
  console.log(args[0]);
}
