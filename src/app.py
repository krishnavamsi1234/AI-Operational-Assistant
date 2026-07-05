from parser import IncidentParser

incident_text = """
Database connection timeout.

CPU usage reached 98%.

Memory usage reached 95%.

Application unavailable.
"""

parser = IncidentParser()

result = parser.parse(incident_text)

print(result)