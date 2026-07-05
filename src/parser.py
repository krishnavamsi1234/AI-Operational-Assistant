"""
Incident Parser Module
"""


class IncidentParser:

    def __init__(self):
        print("Incident Parser Initialized")

    def parse(self, incident_text):

        text = incident_text.lower()

        keywords = []

        category = "Unknown"

        severity = "Low"

        database_words = [
            "database",
            "sql",
            "mysql",
            "oracle",
            "postgres",
            "connection"
        ]

        cpu_words = [
            "cpu",
            "processor",
            "utilization"
        ]

        memory_words = [
            "memory",
            "ram",
            "heap"
        ]

        application_words = [
            "application",
            "service",
            "api"
        ]

        # Keyword Detection

        for word in database_words:
            if word in text:
                keywords.append(word)
                category = "Database"

        for word in cpu_words:
            if word in text:
                keywords.append(word)

        for word in memory_words:
            if word in text:
                keywords.append(word)

        for word in application_words:
            if word in text:
                keywords.append(word)

        # Severity Detection

        if "98%" in text or "95%" in text:

            severity = "Critical"

        incident = {

            "category": category,

            "severity": severity,

            "keywords": keywords,

            "status": "Analyzed"

        }

        return incident