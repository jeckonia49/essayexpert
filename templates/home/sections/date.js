//Default time string PM
const pickerStartedPM = document.querySelector(
  "#timepicker-default-time-string-pm "
);
const tmStartedPM = new te.Timepicker(pickerStartedPM, {
  defaultTime: "02:12 PM"
});

//Default time string AM
const pickerStartedAM = document.querySelector(
  "#timepicker-default-time-string-am"
);
const tmStartedAM = new te.Timepicker(pickerStartedAM, {
  defaultTime: "05:12 AM"
});

//Default time without PM/AM
const pickerStartedWithoutPmAm = document.querySelector(
  "#timepicker-default-time-string-without-pm-am"
);
const tmStartedWithoutPmAm = new te.Timepicker(pickerStartedWithoutPmAm, {
  defaultTime: "05:12"
});

//Default time with 24h
const pickerStartedWith24h = document.querySelector(
  "#timepicker-default-time-string-24h"
);
const tmStartedWith24h = new te.Timepicker(pickerStartedWith24h, {
  defaultTime: "23:44",
  format24: true
});

//Default time date 12h
const pickerStartedWithDate12h = document.querySelector(
  "#timepicker-default-time-with-new-date-12h"
);
const tmStartedWithDate12h = new te.Timepicker(pickerStartedWithDate12h, {
  defaultTime: new Date()
});

//Default time date 24h
const pickerStartedWithDate24h = document.querySelector(
  "#timepicker-default-time-with-new-date-24h"
);
const tmStartedWithDate24h = new te.Timepicker(pickerStartedWithDate24h, {
  defaultTime: new Date(),
  format24: true
});
