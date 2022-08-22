from datetime import datetime 

def add_variable_to_context(request):
    current_datetime = datetime.now().strftime("%d/%m/%Y, %H:%M")  

     
    return{
        'date': current_datetime
    }