/* 
===============================================================
SpreadUtils API

- version: 1
- resource: SpreadApi.gs
- source: https://github.com/fscheidt/dev/blob/master/code/sheets/v1/SpreadApi.js
- libraryId: 1H9Uy_T7DIAlzXQRcCG9rWs7_hjLaoWJP6AdnknOx8UP_-BxEKryjiQdZ

=============================================================== 
*/

var gs = SpreadUtils.getInstance().gs;
var xnr = SpreadUtils.getInstance().xnr;

function getSheetIdByName(shname){ return SpreadUtils.getSheetIdByName(shname) }
function getSheetUrlByName(shname){ return SpreadUtils.getSheetUrlByName(shname) }
function getSheetShortUrlByName(shname){ return SpreadUtils.getSheetShortUrlByName(shname) }

function SHA1(txt,ishort=false){ return SpreadUtils.SHA1(txt,ishort) }
function MD5(txt,isshort=false){ return SpreadUtils.MD5(txt,isshort) }
function UUID(){ return SpreadUtils.UUID() }
function UUID6(){ return SpreadUtils.UUID6() }
function UUID16(){ return SpreadUtils.UUID16() }
function applyBaseTemplate(tplName=null){ return SpreadUtils.applyBaseTemplate(tplName) }
function columnToLetter(){ return SpreadUtils.columnToLetter() }
function clearRangeContent(){ return SpreadUtils.clearRangeContent() }
function clearSheetContent(sh){ return SpreadUtils.clearSheetContent(sh) }
function cloneSheet(){ return SpreadUtils.cloneSheet() }
function copyStyleFromSheet(from,to){ return SpreadUtils.copyStyleFromSheet(from,to) }
function createIndexSheet(){ return SpreadUtils.createIndexSheet() }
function getSheetsNamesAndIds(){ return SpreadUtils.getSheetsNamesAndIds() }
function createSheetFromTemplate(tplName, shName=null){ return SpreadUtils.createSheetFromTemplate(tplName, shName) }
function createNewSheet(clearContent=true){ return SpreadUtils.createNewSheet(clearContent) }
function letterToColumn(){ return SpreadUtils.letterToColumn() }
function extractSSData(){ return SpreadUtils.extractSSData() }
function getDefaultMenuEntries(){ return SpreadUtils.getDefaultMenuEntries() }
function getSSId(){ return SpreadUtils.getSSId() }
function getSSUrl(){ return SpreadUtils.getSSUrl() }
function getSSInfo(){ return SpreadUtils.getSSInfo() }
function getScriptInfo(){ return SpreadUtils.getScriptInfo() }
function getScript(prop="version"){ return SpreadUtils.getScript(prop); }
function getSheets(){ return SpreadUtils.getSheets() }
function getSheetsNames(){ return SpreadUtils.getSheetsNames() }
function getSheetName(){ return SpreadUtils.getSheetName() }
function getSheetHyperLink(){ return SpreadUtils.getSheetHyperLink() }
function getSheetUrl(){ return SpreadUtils.getSheetUrl() }
function getSheetId(){ return SpreadUtils.getSheetId() }
function getSSAllSheetsInfo(){ return SpreadUtils.getSSAllSheetsInfo() }
function getSheetsStartsWith(name){ return SpreadUtils.getSheetsStartsWith(name) }
function getNR(){ return SpreadUtils.getNR() }
function goIndex(shName=null){ return SpreadUtils.goIndex(shName) }
function gotosh(shName){ return SpreadUtils.gotosh(shName) }
function hideAll(startName){ return SpreadUtils.hideAll(startName) }
function hideAllExcept(sheetNames) { return SpreadUtils.hideAllExcept(sheetNames) }
function removeNamedRanges(){ return SpreadUtils.removeNamedRanges() }
function sheetUrlLink(){ return SpreadUtils.sheetUrlLink() }
function showAll(startName=null){ return SpreadUtils.showAll(startName) }
