class TreeNode:
    def __init__(self, name, prompt, children=None):
        self.name = name
        self.prompt = prompt
        self.children = children if children else []


# Example tree structure for the query "How is the Ukraine war shaping anti-drone warfare?"
rag_root = TreeNode(
    "Root",
    "Provide a summary of how the Ukraine war is shaping anti-drone warfare.",
    [
        TreeNode(
            "Use of Drones in Ukraine War",
            "Describe the use of drones in the Ukraine war.",
            [
                TreeNode(
                    "Types of Drones",
                    "What types of drones are being used in the Ukraine war?",
                ),
                TreeNode(
                    "Drone Operations",
                    "How are drones being operated and what roles do they play?",
                )
            ]
        ),
        TreeNode(
            "Anti-Drone Technologies",
            "Describe the anti-drone technologies being developed due to the Ukraine war.",
            [
                TreeNode(
                    "Electronic Jamming",
                    "How is electronic jamming being used to counter drones?",
                ),
                TreeNode(
                    "Kinetic Interceptors",
                    "What are kinetic interceptors and how effective are they?",
                )
            ]
        ),
        TreeNode(
            "Impact on Military Tactics",
            "How has the use of drones influenced military tactics in the Ukraine war?",
            [
                TreeNode(
                    "Adaptations by Ukraine",
                    "How has Ukraine adapted its military tactics in response to drone threats?",
                ),
                TreeNode(
                    "Adaptations by Russia",
                    "How has Russia adapted its military tactics in response to drone threats?",
                )
            ]
        )
    ]
)
