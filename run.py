import dash_core_components as dcc
import dash_html_components as html
import dash
from dash.dependencies import Input, Output, State
import pandas as pd
from flask import Flask
import os


server = Flask(__name__)
server.secret_key = os.environ.get('secret_key', 'secret')
app = dash.Dash(name = __name__, server = server)
app.config.supress_callback_exceptions = True


p_values=[
{'label':'Cristiano Ronaldo','value':'0'},
{'label':'L. Messi','value':'1'},
{'label':'Neymar','value':'2'},
{'label':'L. Suárez','value':'3'},
{'label':'M. Neuer','value':'4'},
{'label':'R. Lewandowski','value':'5'},
{'label':'De Gea','value':'6'},
{'label':'E. Hazard','value':'7'},
{'label':'T. Kroos','value':'8'},
{'label':'G. Higuaín','value':'9'},
{'label':'Sergio Ramos','value':'10'},
{'label':'K. De Bruyne','value':'11'},
{'label':'T. Courtois','value':'12'},
{'label':'A. Sánchez','value':'13'},
{'label':'L. Modrić','value':'14'},
{'label':'G. Bale','value':'15'},
{'label':'S. Agüero','value':'16'},
{'label':'G. Chiellini','value':'17'},
{'label':'G. Buffon','value':'18'},
{'label':'P. Dybala','value':'19'},
{'label':'J. Oblak','value':'20'},
{'label':'A. Griezmann','value':'21'},
{'label':'Thiago','value':'22'},
{'label':'P. Aubameyang','value':'23'},
{'label':'L. Bonucci','value':'24'},
{'label':'J. Boateng','value':'25'},
{'label':'D. Godín','value':'26'},
{'label':'M. Hummels','value':'27'},
{'label':'M. Özil','value':'28'},
{'label':'H. Lloris','value':'29'},
{'label':'Thiago Silva','value':'30'},
{'label':'Z. Ibrahimović','value':'31'},
{'label':'A. Robben','value':'32'},
{'label':'N. Kanté','value':'33'},
{'label':'M. Verratti','value':'34'},
{'label':'P. Pogba','value':'35'},
{'label':'C. Eriksen','value':'36'},
{'label':'A. Vidal','value':'37'},
{'label':'E. Cavani','value':'38'},
{'label':'Marcelo','value':'39'},
{'label':'M. Hamšík','value':'40'},
{'label':'I. Rakitić','value':'41'},
{'label':'David Silva','value':'42'},
{'label':'S. Handanovič','value':'43'},
{'label':'Piqué','value':'44'},
{'label':'Iniesta','value':'45'},
{'label':'H. Kane','value':'46'},
{'label':'J. Rodríguez','value':'47'},
{'label':'Isco','value':'48'},
{'label':'D. Alaba','value':'49'},
{'label':'R. Lukaku','value':'50'},
{'label':'Alex Sandro','value':'51'},
{'label':'T. Müller','value':'52'},
{'label':'Sergio Busquets','value':'53'},
{'label':'Coutinho','value':'54'},
{'label':'M. Reus','value':'55'},
{'label':'T. Alderweireld','value':'56'},
{'label':'David Luiz','value':'57'},
{'label':'Diego Costa','value':'58'},
{'label':'R. Nainggolan','value':'59'},
{'label':'Javi Martínez','value':'60'},
{'label':'D. Mertens','value':'61'},
{'label':'Sokratis','value':'62'},
{'label':'Miranda','value':'63'},
{'label':'K. Benzema','value':'64'},
{'label':'Cesc Fàbregas','value':'65'},
{'label':'F. Ribéry','value':'66'},
{'label':'Pepe','value':'67'},
{'label':'P. Čech','value':'68'},
{'label':'Y. Carrasco','value':'69'},
{'label':'R. Varane','value':'70'},
{'label':'Casemiro','value':'71'},
{'label':'L. Insigne','value':'72'},
{'label':'A. Lacazette','value':'73'},
{'label':'K. Navas','value':'74'},
{'label':'H. Mkhitaryan','value':'75'},
{'label':'D. Subašić','value':'76'},
{'label':'B. Leno','value':'77'},
{'label':'M. ter Stegen','value':'78'},
{'label':'K. Glik','value':'79'},
{'label':'Jordi Alba','value':'80'},
{'label':'I. Gündoğan','value':'81'},
{'label':'Azpilicueta','value':'82'},
{'label':'A. Di María','value':'83'},
{'label':'M. Pjanić','value':'84'},
{'label':'C. Marchisio','value':'85'},
{'label':'J. Vertonghen','value':'86'},
{'label':'B. Matuidi','value':'87'},
{'label':'S. Ruffier','value':'88'},
{'label':'Filipe Luís','value':'89'},
{'label':'V. Kompany','value':'90'},
{'label':'A. Barzagli','value':'91'},
{'label':'E. Bailly','value':'92'},
{'label':'Marco Asensio','value':'93'},
{'label':'Bernardo Silva','value':'94'},
{'label':'A. Laporte','value':'95'},
{'label':'D. Alli','value':'96'},
{'label':'S. Mané','value':'97'},
{'label':'Carvajal','value':'98'},
{'label':'J. Draxler','value':'99'},
{'label':'M. Icardi','value':'100'}]


df = pd.read_csv('pdata.csv',low_memory = False)
df.columns

app.css.append_css({'external_url': 'https://cdn.rawgit.com/plotly/dash-app-stylesheets/2d266c578d2a6e8850ebce48fdb52759b2aef506/stylesheet-oil-and-gas.css'})

app.css.append_css({'external_url': 'https://raw.githubusercontent.com/shashanktmk007/MATCH_PREDICTION-/master/style.css'})
res = df[df.id==0]

app.layout = html.Div([
    html.Div([
        dcc.Dropdown(
        id = 'p_name',
        options =p_values,
            multi= False,
            value='-1'
        )
    ],className = 'row'),
    html.Br(),html.Br(),
    html.Div([
        html.H1('   ',id = 'player_name')
    ],className = 'row'),html.Br(),html.Br(),
          html.Div([  
         ],className = 'row'),
        html.Div([html.Div([html.H5('Age  '),html.H6('',id='player_Age')],className='four columns'),
        html.Div([html.H5('Nationality  '),html.H6('',id='player_Nationality')],className='four columns'),
        html.Div([html.H5('Club  '),html.H6('',id='player_Club')],className='four columns')],className = 'row'),html.Br(),
    html.Div([  
         ],className = 'row'),
        html.Div([html.Div([html.H5('Overall'),html.H6('',id='player_Overall')],className='four columns'),
        html.Div([html.H5('Potential'),html.H6('',id='player_Potential')],className='four columns'),
        html.Div([html.H5('Value'),html.H6('',id='player_Value')],className='four columns')],className = 'row'),html.Br(),
     html.Div([
         html.Div([ html.H5('Wage'), html.H5('   ',id = 'player_Wage')],className='four columns'),
         html.Div([ html.H5('Preferred Positions'), html.H5('   ',id = 'player_PreferredPositions')],className='four columns'),
        # html.Div([ html.H1('Wage'), html.H1('   ',id = 'player_Wage')],className='four columns'),
    ],className = 'row'), html.Br(),    
html.Div([

 html.Div([
        html.Div([html.H5('Heading accuracy'),html.H6('',id='player_Headingaccuracy')] ), 
html.Div([html.H5('Interceptions'),html.H6('',id='player_Interceptions')] ), 
html.Div([html.H5('Jumping'),html.H6('',id='player_Jumping')] ), 
html.Div([html.H5('Long passing'),html.H6('',id='player_Longpassing')] ), 
html.Div([html.H5('Long shots'),html.H6('',id='player_Longshots')] ), 
html.Div([html.H5('Marking'),html.H6('',id='player_Marking')] )
],className='two columns',style={'borderColor':' #57c5f7','borderWidth': 'medium','borderStyle': 'solid','borderRadius': '3.5%','backgroundColor': '#b0b0b05c','padding':'3%','textAlign': 'center','color': 'black'} ),
    html.Div([  
html.Div([html.H5('Composure'),html.H6('',id='player_Composure')] ), 
html.Div([html.H5('Crossing'),html.H6('',id='player_Crossing')] ), 
html.Div([html.H5('Curve'),html.H6('',id='player_Curve')] ), 
html.Div([html.H5('Dribbling'),html.H6('',id='player_Dribbling')] ), 
html.Div([html.H5('Finishing'),html.H6('',id='player_Finishing')] ), 
html.Div([html.H5('Free kick accuracy'),html.H6('',id='player_Freekickaccuracy')] )
],className='two columns',style={'borderColor':' #57c5f7','borderWidth': 'medium','borderStyle': 'solid','borderRadius': '3.5%','backgroundColor': '#b0b0b05c','padding':'3%','textAlign': 'center','color': 'black'}),


html.Div([  html.Div([html.H5('Special'),html.H6('',id='player_Special')] ), 
html.Div([html.H5('Acceleration'),html.H6('',id='player_Acceleration')] ), 
html.Div([html.H5('Aggression'),html.H6('',id='player_Aggression')] ), 
html.Div([html.H5('Agility'),html.H6('',id='player_Agility')] ), 
html.Div([html.H5('Balance'),html.H6('',id='player_Balance')] ), 
html.Div([html.H5('Ball control'),html.H6('',id='player_Ballcontrol')] )],className='two columns',style={'borderColor':' #57c5f7','borderWidth': 'medium','borderStyle': 'solid','borderRadius': '3.5%','backgroundColor': '#b0b0b05c','padding':'3%','textAlign': 'center','color': 'black'}),

html.Div([html.Div([html.H5('Penalties'),html.H6('',id='player_Penalties')] ), 
html.Div([html.H5('Positioning'),html.H6('',id='player_Positioning')] ), 
html.Div([html.H5('Reactions'),html.H6('',id='player_Reactions')] ), 
html.Div([html.H5('Short passing'),html.H6('',id='player_Shortpassing')] ), 
html.Div([html.H5('Shot power'),html.H6('',id='player_Shotpower')] ), 
html.Div([html.H5('Sliding tackle'),html.H6('',id='player_Slidingtackle')] )  ],className='two columns',style={'borderColor':' #57c5f7','borderWidth': 'medium','borderStyle': 'solid','borderRadius': '3.5%','backgroundColor': '#b0b0b05c','padding':'3%','textAlign': 'center','color': 'black'}),
html.Div([
html.Div([html.H5('Sprint peed'),html.H6('',id='player_Sprintspeed')] ),
html.Div([html.H5('Stamina'),html.H6('',id='player_Stamina')] ), 
html.Div([html.H5('Standing ackle'),html.H6('',id='player_Standingtackle')] ), 
html.Div([html.H5('Strength'),html.H6('',id='player_Strength')] ), 
html.Div([html.H5('Vision'),html.H6('',id='player_Vision')] ), 
html.Div([html.H5('Volleys'),html.H6('',id='player_Volleys')] )
 ],className='two columns',style={'borderColor':' #57c5f7','borderWidth': 'medium','borderStyle': 'solid','borderRadius': '3.5%','backgroundColor': '#b0b0b05c','padding':'3%','textAlign': 'center','color': 'black'})


],className = 'row',style={'margin': '#efed51'})
        
        ])
       
@app.callback(Output('player_name','children'),[Input('p_name','value')])
def name(pname):
    p_id = int(pname)
    res = df[df.id==p_id]
    return res.Name
@app.callback(Output('player_Age','children'),[Input('p_name','value')])
def p_Age(pname):
    return df[df.id==int(pname)]['Age']
#
@app.callback(Output('player_Nationality','children'),[Input('p_name','value')])
def p_Nationality(pname):
    return df[df.id==int(pname)]['Nationality']
#
@app.callback(Output('player_Overall','children'),[Input('p_name','value')])
def p_Overall(pname):
    return df[df.id==int(pname)]['Overall']
@app.callback(Output('player_Potential','children'),[Input('p_name','value')])
def p_Potential(pname):
    return df[df.id==int(pname)]['Potential']
@app.callback(Output('player_Club','children'),[Input('p_name','value')])
def p_Club(pname):
    return df[df.id==int(pname)]['Club']
#
@app.callback(Output('player_Value','children'),[Input('p_name','value')])
def p_Value(pname):
    return df[df.id==int(pname)]['Value']
@app.callback(Output('player_Wage','children'),[Input('p_name','value')])
def p_Wage(pname):
    return df[df.id==int(pname)]['Wage']
@app.callback(Output('player_Special','children'),[Input('p_name','value')])
def p_Special(pname):
    return df[df.id==int(pname)]['Special']
@app.callback(Output('player_Acceleration','children'),[Input('p_name','value')])
def p_Acceleration(pname):
    return df[df.id==int(pname)]['Acceleration']
@app.callback(Output('player_Aggression','children'),[Input('p_name','value')])
def p_Aggression(pname):
    return df[df.id==int(pname)]['Aggression']
@app.callback(Output('player_Agility','children'),[Input('p_name','value')])
def p_Agility(pname):
    return df[df.id==int(pname)]['Agility']
@app.callback(Output('player_Balance','children'),[Input('p_name','value')])
def p_Balance(pname):
    return df[df.id==int(pname)]['Balance']
@app.callback(Output('player_Ballcontrol','children'),[Input('p_name','value')])
def p_Ballcontrol(pname):
    return df[df.id==int(pname)]['Ball control']
@app.callback(Output('player_Composure','children'),[Input('p_name','value')])
def p_Composure(pname):
    return df[df.id==int(pname)]['Composure']
@app.callback(Output('player_Crossing','children'),[Input('p_name','value')])
def p_Crossing(pname):
    return df[df.id==int(pname)]['Crossing']
@app.callback(Output('player_Curve','children'),[Input('p_name','value')])
def p_Curve(pname):
    return df[df.id==int(pname)]['Curve']
@app.callback(Output('player_Dribbling','children'),[Input('p_name','value')])
def p_Dribbling(pname):
    return df[df.id==int(pname)]['Dribbling']
@app.callback(Output('player_Finishing','children'),[Input('p_name','value')])
def p_Finishing(pname):
    return df[df.id==int(pname)]['Finishing']
@app.callback(Output('player_Freekickaccuracy','children'),[Input('p_name','value')])
def p_Freekickaccuracy(pname):
    return df[df.id==int(pname)]['Free kick accuracy']
@app.callback(Output('player_Headingaccuracy','children'),[Input('p_name','value')])
def p_Headingaccuracy(pname):
    return df[df.id==int(pname)]['Heading accuracy']
@app.callback(Output('player_Interceptions','children'),[Input('p_name','value')])
def p_Interceptions(pname):
    return df[df.id==int(pname)]['Interceptions']
@app.callback(Output('player_Jumping','children'),[Input('p_name','value')])
def p_Jumping(pname):
    return df[df.id==int(pname)]['Jumping']
@app.callback(Output('player_Longpassing','children'),[Input('p_name','value')])
def p_Longpassing(pname):
    return df[df.id==int(pname)]['Long passing']
@app.callback(Output('player_Longshots','children'),[Input('p_name','value')])
def p_Longshots(pname):
    return df[df.id==int(pname)]['Long shots']
@app.callback(Output('player_Marking','children'),[Input('p_name','value')])
def p_Marking(pname):
    return df[df.id==int(pname)]['Marking']
@app.callback(Output('player_Penalties','children'),[Input('p_name','value')])
def p_Penalties(pname):
    return df[df.id==int(pname)]['Penalties']
@app.callback(Output('player_Positioning','children'),[Input('p_name','value')])
def p_Positioning(pname):
    return df[df.id==int(pname)]['Positioning']
@app.callback(Output('player_Reactions','children'),[Input('p_name','value')])
def p_Reactions(pname):
    return df[df.id==int(pname)]['Reactions']
@app.callback(Output('player_Shortpassing','children'),[Input('p_name','value')])
def p_Shortpassing(pname):
    return df[df.id==int(pname)]['Short passing']
@app.callback(Output('player_Shotpower','children'),[Input('p_name','value')])
def p_Shotpower(pname):
    return df[df.id==int(pname)]['Shot power']
@app.callback(Output('player_Slidingtackle','children'),[Input('p_name','value')])
def p_Slidingtackle(pname):
    return df[df.id==int(pname)]['Sliding tackle']
@app.callback(Output('player_Sprintspeed','children'),[Input('p_name','value')])
def p_Sprintspeed(pname):
    return df[df.id==int(pname)]['Sprint speed']
@app.callback(Output('player_Stamina','children'),[Input('p_name','value')])
def p_Stamina(pname):
    return df[df.id==int(pname)]['Stamina']
@app.callback(Output('player_Standingtackle','children'),[Input('p_name','value')])
def p_Standingtackle(pname):
    return df[df.id==int(pname)]['Standing tackle']
@app.callback(Output('player_Strength','children'),[Input('p_name','value')])
def p_Strength(pname):
    return df[df.id==int(pname)]['Strength']
@app.callback(Output('player_Vision','children'),[Input('p_name','value')])
def p_Vision(pname):
    return df[df.id==int(pname)]['Vision']
@app.callback(Output('player_Volleys','children'),[Input('p_name','value')])
def p_Volleys(pname):
    return df[df.id==int(pname)]['Volleys']
@app.callback(Output('player_PreferredPositions','children'),[Input('p_name','value')])
def p_PreferredPositions(pname):
    return df[df.id==int(pname)]['Preferred Positions']
if __name__ == '__main__':
    app.run_server()
