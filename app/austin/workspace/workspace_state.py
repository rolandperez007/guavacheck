"""
Austin Workspace State

Represents everything currently open inside Austin.

Open Property

Open Workflow

Selected District

Active Simulation

Current Conversation

Pinned Insights

Draft Reports

Pending Actions

Running Tasks

Uploads

Voice Session

Institution Workspace
"""


class WorkspaceState:

    def __init__(self):

        self.active_property = None

        self.active_workflow = None

        self.selected_district = None

        self.pending_actions = []

        self.running_tasks = []

        self.uploads = []

        self.insights = []

        self.voice_enabled = False