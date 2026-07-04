from parser import IncidentParser
incident_text = """ 
Database connection timeout.
CPU usage reached 98% for the last 5 minutes.
Memory usage is at 95% capacity.
Application unavilable."""

parser = IncidentParser()
result = parser.parse(incident_text)
print(result)