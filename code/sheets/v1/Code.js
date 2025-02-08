const sf = {
  INDEX: `index`,
  VAR: `vars`,
}
const appSheets = [
  sf.INDEX
]

/* =========================================== */
const scriptID = "SS_SCRIPT_ID";
var sheetScript = {
  name: "PROJECT_NAME",
  script_url: `https://script.google.com/u/0/home/projects/${scriptID}/edit`,
  script_id: scriptID,
  version: "1.0",
  uuid: "unique",
  repo: `https://github.com/fscheidt/dev/blob/master/code/sheets/v1/SpreadApi.js`,
}
/* =========================================== */
function createAva(){ copySheet("ava"); }
function createBlank(){ copySheet("blank"); }
function createCalendar(){ copySheet("calendar"); }
function createIndex(){ copySheet("index"); }
function createDisciplinas(){ copySheet("disciplinas"); }
function createConsulta(){ copySheet("consulta"); }
function createDados(){ copySheet("dados"); }
function createExporta(){ copySheet("exporta"); }
function createEnums(){ copySheet("enums"); }
function createVars(){ copySheet("vars"); }
function createView(){ copySheet("view"); }

function onOpen() {
  var ss = SpreadsheetApp.getActive();
  var entries = getDefaultMenuEntries();
  entries.push(
    { name: "import: ava", functionName: "createAva" },
    { name: "import: calendar", functionName: "createCalendar" },
    { name: "import: disciplinas", functionName: "createDisciplinas" },
    null,
    { name: "create: blank", functionName: "createBlank" },
    { name: "create: index", functionName: "createIndex" },
    { name: "create: consulta", functionName: "createConsulta" },
    { name: "create: dados", functionName: "createDados" },
    { name: "create: exporta", functionName: "createExporta" },
    { name: "create: enums", functionName: "createEnums" },
    { name: "create: vars", functionName: "createVars" },
    { name: "create: view", functionName: "createView" },
    { name: "style: highlight formulas", functionName: "highlightFormulas" },
    null,
    { name: "admin: prompt permissions", functionName: "promptAuth" },
  )
  ss.addMenu("⌘ Menu", entries);
}
/* =========================================== */