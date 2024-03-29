const fs = require('fs');
const path = require('path');
const csv = require('csv-parser');

const rootDirectory = path.dirname(__file__);
const dataFile = path.join(rootDirectory, '2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv');

const colorCount = {};

fs.createReadStream(dataFile)
  .pipe(csv())
  .on('data', (row) => {
    const furColor = row['Primary Fur Color'];
    colorCount[furColor] = (colorCount[furColor] || 0) + 1;
  })
  .on('end', () => {
    const newData = [['Fur Color', 'Count']];
    for (const color in colorCount) {
      newData.push([color, colorCount[color]]);
    }

    const outputFile = path.join(rootDirectory, 'squirrel_count.csv');
    const csvData = newData.map((row) => row.join(',')).join('\n');

    fs.writeFile(outputFile, csvData, (err) => {
      if (err) throw err;
      console.log('Data written to squirrel_count.csv');
    });
  });