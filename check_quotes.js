const fs = require('fs');
const content = fs.readFileSync('js/data.js', 'utf8');
const lines = content.split('\n');

// Try to parse and find errors
try {
  new Function(content);
  console.log('No syntax errors found!');
} catch(e) {
  console.log('Syntax error:', e.message);
}

// Find lines with potential nested quote issues
// A string value in this file looks like: text: "...content..."
// or body: "...content..."
// We need to find lines where there are unescaped " inside the value

lines.forEach((line, i) => {
  const trimmed = line.trim();
  // Skip comments and non-data lines
  if (trimmed.startsWith('//') || trimmed.startsWith('/*') || trimmed.startsWith('*') || trimmed.startsWith('const') || trimmed.startsWith('];')) return;
  
  // Count double quotes in the line
  // A normal data line should have an even number of " (key-value pairs)
  // If there's an odd number or extra quotes inside values, it's problematic
  
  // More precise: find patterns like: "..." inside the value portion
  // Let's look for lines that have text between colons and closing brace
  const match = trimmed.match(/\w+:\s*"(.*)"\s*[,}\]]/);
  if (match) {
    const value = match[1];
    if (value.includes('"')) {
      console.log(`Line ${i+1}: ${trimmed.substring(0, 120)}`);
    }
  }
});
