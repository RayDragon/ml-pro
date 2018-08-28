// For basic server i/o management

$(document).ready(()=>{
    // on loading request for all sources ... list
    $.get('/add_task');
    load();

});
function load(){
    $.get('/get_task', (data, status)=>{
        if(got_data.length==0) got_data=data;
        console.log(data);
        data = JSON.parse(data);
        for(var i=0;i<data.length;i++){
            
            if(data[i].name == 'source_updated'){
                // we need to update our source with new values
                s = JSON.parse(data[i].values);
                for(var ii=0;ii<s.length;ii++){
                    var b;
                    for(b in s[ii])break;
                    //console.log(b,s[ii][b]);
                    srcs.append(new Source(b, s[ii][b]));
                }
                
            }else if(data[i].name == 'derived_updated'){
                // we need to update our source with new values
                s = JSON.parse(data[i].values);
                for(d in s){
                    //console.log(s[d].name);
                    drds.append(new Derived(s[d].name, s[d].x, s[d].fx));
                }
                
            }else if(data[i].name == 'outcome_updated'){
                // we need to update our source with new values
                s = JSON.parse(data[i].values);
                for(var ii=0;ii<s.length;ii++){
                    var b;
                    for(b in s[ii])break;
                    //console.log(b,s[ii][b]);
                    otcs.append(new Source(b, s[ii][b]));
                }
                
            }
        }
        
    });
}
got_data=[]
setInterval(()=>{
    // this will run every 5 seconds to retrive
    // data from the server
    load();

}, 5000);
class Sources{
    constructor(){
        this.list=[];
    }
    append(s=Source('', [])){
        this.list.push(s);
        $('#sources_table_body').append(s.get_html());
        
    }
}
srcs = new Sources();
class Source{
    /*
    'name':'SourceName',
    'cols':[],
    create_source:(name='Source_Name', cols=['col1', 'col2', 'col3'])=>{
        this.name = name;
        this.cols=cols;
    }*/
    constructor(name='Source_Name', cols=['col1', 'col2', 'col3']){
        this.name = name;
        this.cols = cols;
    }
    comma_sep_cols(){
        var v='';
        for(var i=0;i<this.cols.length;i++){
            v+=this.cols[i];
            if(this.cols.length-i!=1)v+=', ';
        }
        return v;
    }
    get_html() {
        var html=['<tr><td class="mdl-data-table__cell--non-numeric">',
        '</td><td class="mdl-data-table__cell--non-numeric">',
        '</td><td class="mdl-data-table__cell--non-numeric"></td></tr>'];
        return html[0]+this.name+html[1]+this.comma_sep_cols()+html[2];
    } 
}

class Outcomes{
    constructor(){
        this.list=[];
    }
    append(s=Source('', [])){
        this.list.push(s);
        $('#outcome_table_body').append(s.get_html()); 
        
    }
}
otcs = new Outcomes();
class Outcome{
    /*
    'name':'SourceName',
    'cols':[],
    create_source:(name='Source_Name', cols=['col1', 'col2', 'col3'])=>{
        this.name = name;
        this.cols=cols;
    }*/
    constructor(name='Outcome_Name', cols=['col1', 'col2', 'col3']){
        this.name = name;
        this.cols = cols;
    }
    comma_sep_cols(){
        var v='';
        for(var i=0;i<this.cols.length;i++){
            v+=this.cols[i];
            if(this.cols.length-i!=1)v+=', ';
        }
        return v;
    }
    get_html() {
        var html=['<tr><td class="mdl-data-table__cell--non-numeric">',
        '</td><td class="mdl-data-table__cell--non-numeric">',
        '</td><td class="mdl-data-table__cell--non-numeric">'+
        '</td></tr>'];
        return html[0]+this.name+html[1]+this.comma_sep_cols()+html[2];
    } 
}













class Deriveds{
    constructor(){
        this.list=[];
    }
    append(s=Derived('', [])){
        this.list.push(s);
        $('#derived_table_body').append(s.get_html());
        
    }
}
drds = new Deriveds();
class Derived{
    constructor(name='Derived_Name', x='column_name', fx='function of x'){
        this.name = name;
        this.x = x;
        this.fx=fx
    }
    get_html() {
        var html=['<tr><td class="mdl-data-table__cell--non-numeric">',
        '</td><td class="mdl-data-table__cell--non-numeric">',
        '</td><td class="mdl-data-table__cell--non-numeric">',
        '</td><td class="mdl-data-table__cell--non-numeric">'+
        '</td></tr>'];
        return html[0]+this.name+html[1]+this.x+html[2]+this.fx+html[3];
    } 
}




