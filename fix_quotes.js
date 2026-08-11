const fs = require('fs');
const content = fs.readFileSync('js/data.js', 'utf8');
const lines = content.split('\n');

let problemLines = [];

lines.forEach((line, i) => {
  const trimmed = line.trim();
  // Skip comments and non-data lines
  if (trimmed.startsWith('//') || trimmed.startsWith('/*') || trimmed.startsWith('*') || trimmed.startsWith('const') || trimmed.startsWith('];') || trimmed === '') return;
  
  // For each line, we need to find string values and check for unescaped inner quotes
  // A string value looks like: key: "value"
  // The issue is when "value" contains unescaped " characters
  
  // Strategy: count the number of " in the line (excluding escaped \")
  // For a valid data line, the count should be even
  const unescapedQuotes = (line.match(/(?<!\\)"/g) || []).length;
  if (unescapedQuotes % 2 !== 0) {
    problemLines.push({ lineNum: i+1, line: trimmed.substring(0, 150) });
  }
});

console.log('=== Lines with odd number of quotes (likely broken) ===');
problemLines.forEach(p => {
  console.log(`Line ${p.lineNum}: ${p.line}`);
});
console.log(`\nTotal problem lines: ${problemLines.length}`);
