from enum import Enum
from typing import List, Set, Type

from singer_sdk.streams.core import Stream

from tap_github.organization_streams import (
    OrganizationStream,
    TeamMembersStream,
    TeamRolesStream,
    TeamsStream,
)
from tap_github.repository_streams import (
    AnonymousContributorsStream,
    AssigneesStream,
    CollaboratorsStream,
    CommitCommentsStream,
    CommitsStream,
    CommunityProfileStream,
    ContributorsStream,
    DependenciesStream,
    DependentsStream,
    EventsStream,
    ExtraMetricsStream,
    IssueCommentsStream,
    IssueEventsStream,
    IssuesStream,
    LanguagesStream,
    MilestonesStream,
    ProjectCardsStream,
    ProjectColumnsStream,
    ProjectsStream,
    PullRequestCommits,
    PullRequestFiles,
    PullRequestsStream,
    ReadmeHtmlStream,
    ReadmeStream,
    ReleasesStream,
    RepositoryStream,
    ReviewCommentsStream,
    ReviewsStream,
    StargazersGraphqlStream,
    StargazersStream,
    StatsContributorsStream,
    WorkflowRunJobsStream,
    WorkflowRunsStream,
    WorkflowsStream,
)
from tap_github.user_streams import StarredStream, UserContributedToStream, UserStream


class Streams(Enum):
    """
    Represents all streams our tap supports, and which queries (by username, by organization, etc.) you can use.
    """

    valid_queries: Set[str]
    streams: List[Type[Stream]]

    def __init__(self, valid_queries: Set[str], streams: List[Type[Stream]]):
        self.valid_queries = valid_queries
        self.streams = streams

    REPOSITORY = (
        {"repositories", "organizations", "searches"},
        [
            AnonymousContributorsStream,
            AssigneesStream,
            CollaboratorsStream,
            CommitCommentsStream,
            CommitsStream,
            CommunityProfileStream,
            ContributorsStream,
            DependenciesStream,
            DependentsStream,
            EventsStream,
            IssueCommentsStream,
            IssueEventsStream,
            IssuesStream,
            LanguagesStream,
            MilestonesStream,
            ProjectCardsStream,
            ProjectColumnsStream,
            ProjectsStream,
            PullRequestCommits,
            PullRequestFiles,
            PullRequestsStream,
            ReadmeHtmlStream,
            ReadmeStream,
            ReleasesStream,
            ExtraMetricsStream,
            RepositoryStream,
            ReviewCommentsStream,
            ReviewsStream,
            StargazersGraphqlStream,
            StargazersStream,
            StatsContributorsStream,
            WorkflowRunJobsStream,
            WorkflowRunsStream,
            WorkflowsStream,
        ],
    )
    USERS = (
        {"user_usernames", "user_ids"},
        [
            StarredStream,
            UserContributedToStream,
            UserStream,
        ],
    )
    ORGANIZATIONS = (
        {"organizations"},
        [OrganizationStream, TeamMembersStream, TeamRolesStream, TeamsStream],
    )

    @classmethod
    def all_valid_queries(cls):
        return set.union(*[stream.valid_queries for stream in Streams])
