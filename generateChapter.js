//Require File System in node
var fs = require('fs');
//Read git URL to get md from other book; write MD to root path, e.g. ./CADGIS0About/0.00.About.md
function generateChapter(readURL,writeMD) {
  //Read md file from git
  var chapter = fs.readFile(readURL, 'utf-8', (err, data) {
                              // err will be an error object if an error occured
                              // data will be the file that was read
                              console.log(data);
                              }
                            );
  //Write md file from git
  fs.writeFileSync(writeMD, markdownReadMe);
};
