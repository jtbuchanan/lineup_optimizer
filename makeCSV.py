import pandas as pd

def merge_data(rw_QbRbWrTe, rw_K, fd):
    # Remove all unnecessay columns
    rw_QbRbWrTe = rw_QbRbWrTe.drop(['Opponent','Spread','OverUnder','Comp','Att','PassYards','PassTD','PassInt','RushAtt','RushYards','RushTD','Rec','RecYards','RecTD'], axis=1)
    rw_K = rw_K.drop(['Opponent','Spread','OverUnder','FGM','FGA','XPM','XPA'], axis=1)
    fd = fd.drop(['Id','Played','Game','Opponent','Unnamed: 12','Unnamed: 13'], axis=1)

    # Now that both DFs from rotowire sources have the same columns, concatenate them together.
    rotowire = pd.concat([rw_QbRbWrTe,rw_K])

    # There are now two DFs 'rotowire' and 'fd'. In each of the DFs create a playerID column to merge on.
    rotowire["playerID"] =  rotowire[['Last Name', 'First Name','Team','Pos']].fillna('').sum(axis=1)
    fd["playerID"] = fd[['Last Name','First Name','Team','Position']].fillna('').sum(axis=1)

    # After the playerID is created drop the no longer needed columns from the 'rotowire' DF.
    rotowire = rotowire.drop(['Last Name', 'First Name','Team','Pos'], axis=1)

    # Pull out all D teams from fd to fd_d
    fd_d = fd[fd['Position'] == 'D'].copy()
    # Populate 'FantasyPts' with the values from 'FPPG'
    fd_d['FantasyPts'] = fd_d['FPPG']

    # Merge the two DFs together on playerID
    merged = fd.merge(rotowire, on='playerID')

    # concat fd_d to merged.  
    merged = pd.concat([merged,fd_d])

    # Create the name column and rename other columns as necessary for use in optimize.py
    merged["name"] = merged[['First Name', 'Last Name']].fillna('').sum(axis=1)
    merged = merged.rename(columns={'Team': 'team', 'Salary': 'salary', 'FantasyPts': 'points', 'Position':'position_text'})
    # Move the name column to the front.
    merged = order(merged, ['name'])


    # Export results to csv
    merged.to_csv("magic.csv", index=False)

def order(frame,var):
    varlist =[w for w in frame.columns if w not in var]
    frame = frame[var+varlist]
    return frame 

if __name__=='__main__':
	 # Read the three CSV source files.
    rw_QbRbWrTe = pd.read_csv("rw_QbRbWrTe.csv")
    rw_K = pd.read_csv("rw_K.csv")
    fd = pd.read_csv("fd.csv")

    merge_data(rw_QbRbWrTe, rw_K, fd)

