class RoleBuilder:
    """
    Private data member
    """
    ROLES = ["UNDEFINED", "DEVELOPER", "TEST_ENGINEER", "SR_DEVELOPER", "DESIGNER"]

    """
    Method to get role description for a given role id
    """
    @staticmethod
    def get_role_description(role_id):
        if 1 <= role_id < len(RoleBuilder.ROLES):
            return RoleBuilder.ROLES[role_id]
        else:
            return RoleBuilder.ROLES[0]
