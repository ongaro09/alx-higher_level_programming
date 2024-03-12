#!/usr/bin/node

const args = process.argv.slice(2);

if (args.length === 0) {
  console.log('No argument');
} else if (args.length === 1) {
  for (const arg of args) {
    console.log(arg);
  }
}
