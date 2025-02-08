const sf = {
  INDEX: `index`,
  VAR: `vars`,
}
const appSheets = [
  sf.INDEX
]

/* =========================================== */

var SCRIPT = {
  url: "https://script.google.com/u/0/home/projects/<LIBRARY_ID>/edit",
  name: "SPREADSHEET_NAME",
  version: "1.1",
  uuid: "0x",
  repo: ``,
  ss: `https://docs.google.com/spreadsheets/d/<SPREADSHEET_ID>`,
}

/* =========================================== */

function onOpen() {
  var ss = SpreadsheetApp.getActive();
  var entries = getDefaultMenuEntries();
  /*
  entries.push(
    { name : "🆕 Clone Sheet", functionName : "clone"}
  )
  */
  ss.addMenu("Menu", entries);
}

/* =========================================== */
