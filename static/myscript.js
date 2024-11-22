
$(document).ready(function() { 
    for (let year = startYear; year <= endYear; year++) {
      document.write('<option value="' + year + '">' + year + '</option>');
    }
})