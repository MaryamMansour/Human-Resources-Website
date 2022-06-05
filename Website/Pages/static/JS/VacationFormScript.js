
// don't forget to make textarea (reason) required

function validateForm() {

    validateFormDates()
}


function validateFormDates()
{
    let sd = new Date(document.getElementById('sd').value);
    let ed = new Date(document.getElementById('ed').value);
    sd.setHours(0,0,0,0);
    ed.setHours(0,0,0,0);
    
    console.log(ed," - ",sd," = ",sd-ed);
    
    let currentDate = new Date();
        
        // 3456000000 Milliseconds = 40 days  // Maximum number of days to take off is 40 days. (:(:(: more than that you are fired :):):)
        if( ed > sd && ed-sd <= 3456000000 && sd > currentDate && ed > currentDate )
        {
            alert('The Vacation Form Is Submitted Successfully');
        }
        else
        {
            console.log("ed > sd : "             + (ed > sd) );
            console.log("ed-sd <= 2629800000 : " + (ed-sd <= 2629800000) );
            console.log("sd > currentDate : "    + (sd > currentDate) );
            console.log("ed > currentDate : "    + (ed > currentDate));
            
            alert('Submission Failed, Enter Dates Correctly');
        }
    
    
}

