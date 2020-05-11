from django.shortcuts import render
import pandas as pd

# Create your views here.
def index(request):
    template_name="index.html"
    
    # Read data from CSV using Python Pandas
    df=pd.read_csv("data/car_sales.csv")
    rs = df.groupby("Engine size")["Sales in thousands"].agg("sum")
    categories = list(rs.index)
    values = list(rs.values)
    table_content = df.to_html(index=None)
    table_content = table_content.replace('class="dataframe"',"class='table table-striped'")
    table_content = table_content.replace('border="1"',"")
    context={
        'categories': categories,
        'values': values,
        'table_data': table_content,
    }
    
    return render(request, template_name, context)