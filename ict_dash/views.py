# imports from django modules and libraries
from django.shortcuts import render
from django.views.generic import TemplateView
from math import pi
import pandas as pd
from django.db.models import Count, Q, F

# imports from custom modules
from ict_contracts.models import Contract   
from ict_licenses.models import License
from ict_projects.models import Project
from ict_vendors.models import Vendor 
from ict_accounts.models import Account

#imports form bokeh
from bokeh.plotting import figure, show
from bokeh.embed import components
from bokeh.models import ColumnDataSource, NumeralTickFormatter, PrintfTickFormatter
from bokeh.models.tools import HoverTool
from bokeh.transform import factor_cmap, cumsum
from bokeh.palettes import (Greens5, GnBu5, Reds5, Blues5, Category20c,
                        Category20_10, Category20c, Category10_3, 
                        Vibrant3, Spectral10, Cividis, Category20b_3
                        )


# Views functionality for the dashboard graphs.
def dash(request):
    num_contracts = Contract.objects.all().count()
    num_licenses = License.objects.all().count()
    num_projects = Project.objects.all().count()
    num_vendors = Vendor.objects.all().count()
    num_users = Account.objects.all().count()
      
    locations = Contract.objects.order_by('supplier__location_footprint').values_list(
                            'supplier__location_footprint').annotate(
                                locations = Count('supplier__location_footprint')
                            )
    print('LOCATIONS :',locations)
    x = dict(locations)
    
    data = pd.Series(x).reset_index(name='value').rename(columns={'index': 'locality'})
    print(data)
    print('@'*25)
    print('Len Data :',len(data))
    print('Len X :',len(x))
    print('@'*25)
    
    data['angle'] = data['value']/data['value'].sum() * 2*pi
    data['color'] = None if len(data) == 0 else Category10_3
    
    p3 = figure(height=350, width=600, title="ICT Contracts by Supplier Nationality Footprint", toolbar_location=None,
           tools="hover", tooltips="@locality: @value", x_range=(-0.5, 1.0))
    
    p3.wedge(x=0, y=1, radius=0.4, 
        start_angle=cumsum('angle', include_zero=True), end_angle=cumsum('angle'),
        line_color="white", fill_color='color', legend_field='locality', source=data)
    
    p3.axis.axis_label = None
    p3.axis.visible = False
    p3.grid.grid_line_color = None
    p3.title.align = 'center'
    
    # show(p3)
    

    
    print('DATA DICT :',data)
    nationailty_list = [ n[0] for n in locations]
    nationality_counts = [c[1] for c in locations ]
    
    
    
# Plotting Contracts values for horizontal bar graph graph
    contracts = Contract.objects.order_by('total_value')
    count = len(contracts)
    contract_names = [c.name for c in contracts][-5:count]
    total_values = [int(v.total_value) for v in contracts][-5:count]
    print(contract_names)
    print(total_values)
    contract_type = [v.agreement_type for v in contracts][-5:count]
    supplier = [v.supplier.name for v in contracts][-5:count]
    duration = [v.duration for v in contracts][-5:count]
    location = [v.supplier.location_footprint for v in contracts][-5:count]
    
    
    source = ColumnDataSource(data = dict(contract_names=contract_names, 
                                          total_values=total_values,
                                          supplier=supplier,
                                          contract_type=contract_type,
                                          duration=duration,
                                          location=location,
                                          )
                              )
   
    p = figure(y_range = contract_names, width=600, height=300, 
               title="Top 5 Contracts by Total Term Value",  toolbar_location=None, tools="")
    p.hbar(y='contract_names', right='total_values', height=0.5, 
           source=source, 
        #    legend_field = 'total_values',
           fill_color=factor_cmap(
               'contract_names',
palette=None if len(data) == 0 else Blues5,
               factors=contract_names,
           ),
           fill_alpha=0.9,
        )
    
    p.title.align = 'center'
    p.xaxis.formatter = PrintfTickFormatter(format="R%0.2i ")
    # p.legend.orientation = 'horizontal'
    # p.legend.location = 'top'
    # p.legend.label_text_font_size = '10px'
   
    # p.xaxis.formatter = NumeralTickFormatter(format="0.0 %s")
    
    hover1 = HoverTool()
    hover1.tooltips = """
    <div style = "background-color:rgb(4, 26, 61); color:#fff" width=250, height=250 >
        <!--<img src="@logo" alt="" height=40 width=60 >--!>
       <h3><strong >Vendor: </strong>@supplier</h3>
       <h3 style="color:orange"> <strong  >Total Value: </strong> R@total_values</h3>  
    </div> 
    """
    p.add_tools(hover1)
    
    script, div = components(p)
    
#Plotting Licenses values graph
    count = License.objects.count()
    
    licenses = License.objects.order_by('current_cost')
    
    license_names = [c.name for c in licenses][-5:count]
    current_values = [int(v.current_cost) for v in licenses][-5:count]
    categories = [cat.software_category for cat in licenses][-5:count]
    vendor = [v.service_provider.name for v in licenses][-5:count]
    location = [v.service_provider.location_footprint for v in licenses][-5:count]
    # price = [v.service_provider.name for v in licenses][-1:count]
    
    # print('*'*30)
    # print(license_names)
    # print(current_values)
    # print('-'*30)
    
    source = ColumnDataSource(data = dict(license_names=license_names, 
                                          current_values=current_values,
                                          categories = categories,
                                          vendor=vendor,
                                          location=location,
                                          )
                              )
   
    p2 = figure(y_range = license_names, width=600, height=300, 
                title="Top 5 licenses by Current Value",  toolbar_location=None, tools="")
    p2.hbar(y='license_names', right='current_values', height=0.5, 
            source=source, 
            # legend_field='current_values',
            fill_color=factor_cmap(
               'license_names',
               palette= None if len(license_names) == 0 else Reds5,
               factors=license_names,
               
           ), 
            fill_alpha=0.9
        )
    
    p2.title.align = 'center'
 
    p2.xaxis.formatter = PrintfTickFormatter(format="R%0.2i ")
    
    # Tooltips
    hover = HoverTool()
    hover.tooltips = """
        <div style = "background-color:rgb(4, 26, 61); color:#fff" width=250, height=250 >
            <!--<img src="@logo" alt="" height=40 width=60 >--!>
        <h3><strong >Service Provider: </strong>@vendor</h3>
        <h3 style="color:orange"> <strong  >Current Cost: </strong> R@current_values</h3>  
        </div>   
    """
    p2.add_tools(hover)
    
# Projects graph
    try:
        pass
    except:
        pass
    
    projects = Project.objects.order_by('total_cost')
    print('LEGNTH OF PROJECTS : ',len(projects))
    project_names = [c.name for c in projects][-5:count]

    project_total_value = [int(v.total_cost) for v in projects][-5:count]
    project_vendor = [v.service_provider.name for v in projects][-5:count]
    print(project_names)
    print(project_total_value)
    print(project_vendor)
    source = ColumnDataSource(data = dict(project_names=project_names, 
                                          project_total_value=project_total_value,
                                          project_vendor = project_vendor,
                                          )
                              )
    
    p4 = figure(width=600, height=300, 
                title="Top 5 Projects by Total Cost",  toolbar_location=None, tools="")
    p4.vbar(x='project_names', top='project_total_value', bottom=0, width=0.5, 
            source=source, 
            # legend_field='current_values',

            fill_color=factor_cmap(
               'project_names',
               palette=None if len(data) == 0 else Cividis[len(data)],
               factors=project_names,           
           ), 
    fill_alpha=0.9
        )
    
    p4.title.align = 'center'
    p4.xaxis.formatter = PrintfTickFormatter(format="R%0.2i ")
    
    hover4 = HoverTool()
    hover4.tooltips = """
        <div style = "background-color:rgb(4, 26, 61); color:#fff" width=250, height=250 >
            <!--<img src="@logo" alt="" height=40 width=60 >--!>
        <h3><strong >Service Provider: </strong>@project_vendor</h3>
        <h3 style="color:orange"> <strong  >Total Cost: </strong> R@project_total_value</h3>  
        </div>   
    """
    p4.add_tools(hover4)
    
    
    script, div = components(p)
    script2, div2 = components(p2)
    script3, div3 = components(p3)
    script4, div4 = components(p4)
      
    context = {
        'num_contracts': num_contracts,
        'num_licenses': num_licenses,
        'num_projects': num_projects,
        'num_vendors': num_vendors,  
        'num_users': num_users,
        'div': div,
        'script': script,
        'div2': div2,
        'script2': script2,
        'div3':div3,
        'script3':script3,
        'div4':div4,
        'script4':script4,
    }
    return render(request, 'ict_dash/dashboard.html', context)
    
class ContractValueView(TemplateView):
    model = Contract
    template_name = "ict_dash/dash.html"
     
    def get_context_data(self, *args, **kwargs):
        context = super(ContractValueView, self).get_context_data(*args, **kwargs)
        
        context['contract_name_list'] = [item[0] for item in Contract.objects.values_list('name').order_by('-total_value')]
        context['contract_value_list'] = [int(item[0]) for item in Contract.objects.values_list('total_value').order_by('-total_value')]
        return context
