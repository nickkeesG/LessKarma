POST_MINIMAL_SCHEMA = """
    {
      posts(input: {
        terms: {
          view: "new"
          limit: 2
          meta: null  # this seems to get both meta and non-meta posts
        }
      }) {
        results {
          _id
          title
          slug
          pageUrl
        #   url
        #   createdAt
        status
        isFuture
          postedAt
          sticky
          stickyPriority
          meta
          question
        #   votingSystem
          baseScore
          afBaseScore
        #   extendedScore
        #   afExtendedScore
          score
          voteCount
          allVotes {
            #   userId
              voteType
            #   extendedVoteType
            #   power
            #   afPower
              cancelled
              isUnvote
            #   votedAt
          }
        #   viewCount
          wordCount
          htmlBody
          user {
            username
            slug
          }
          hideAuthor
          commentCount
          afCommentCount
          af
        }
      }
    }
"""

POST_FULL_SCHEMA = """
    {{
      posts(input: {{
        terms: {{
          view: "old"
          limit: {limit}
          offset: {offset}
          meta: null  # this seems to get both meta and non-meta posts
        }}
      }}) {{
        results {{
            createdAt
            postedAt
            modifiedAt
            url
            title
            slug
            viewCount
            lastCommentedAt
            clickCount
            deletedDraft
            status
            isFuture
            sticky
            stickyPriority
            userIP
            userAgent
            referrer
            author
            user {{
              username
              # bio # bio is available but not yet necessary for the dataset
              # htmlBio
              # emails
              createdAt
              isAdmin
              # profile
              displayName
              # previousDisplayName
            }}
            userId
            domain
            pageUrl
            pageUrlRelative
            linkUrl
            postedAtFormatted
            emailShareUrl
            twitterShareUrl
            facebookShareUrl
            socialPreviewImageUrl
            question
            authorIsUnreviewed
            wordCount
            htmlBody
            submitToFrontpage
            hiddenRelatedQuestion
            originalPostRelationSourceId
            # sourcePostRelations
            # targetPostRelations
            shortform
            canonicalSource
            nominationCount2018
            nominationCount2019
            reviewCount2018
            reviewCount2019
            reviewCount
            reviewVoteCount
            positiveReviewVoteCount
            reviewVoteScoreAF
            reviewVotesAF
            reviewVoteScoreHighKarma
            reviewVotesHighKarma
            reviewVoteScoreAllKarma
            reviewVotesAllKarma
            finalReviewVoteScoreHighKarma
            finalReviewVotesHighKarma
            finalReviewVoteScoreAllKarma
            finalReviewVotesAllKarma
            finalReviewVoteScoreAF
            finalReviewVotesAF
            lastCommentPromotedAt
            # tagRel(tagId)
            # tags
            tagRelevance
            # lastPromotedComment
            # bestAnswer
            noIndex
            rsvps
            activateRSVPs
            nextDayReminderSent
            onlyVisibleToLoggedIn
            onlyVisibleToEstablishedAccounts
            # currentUserReviewVote
            votingSystem
            myEditorAccess
            _id
            schemaVersion
            currentUserVote
            currentUserExtendedVote
            # currentUserVotes
            allVotes {{
              # userId
              voteType
              # extendedVoteType
              # power
              # afPower
              cancelled
              isUnvote
              # votedAt
            }}
            voteCount
            baseScore
            extendedScore
            score
            legacy
            legacyId
            legacySpam
            # feed
            feedId
            feedLink
            lastVisitedAt
            isRead
            curatedDate
            metaDate
            suggestForCuratedUsernames
            suggestForCuratedUserIds
            frontpageDate
            collectionTitle
            # coauthors
            coauthorUserIds
            socialPreviewImageId
            socialPreviewImageAutoUrl
            # canonicalSequence
            canonicalSequenceId
            # canonicalCollection
            canonicalCollectionSlug
            # canonicalBook
            canonicalBookId
            canonicalNextPostSlug
            canonicalPrevPostSlug
            # nextPost(sequenceId)
            # prevPost(sequenceId)
            # sequence(sequenceId)
            unlisted
            disableRecommendation
            defaultRecommendation
            draft
            meta
            hideFrontpageComments
            maxBaseScore
            # scoreExceeded2Date
            # scoreExceeded30Date
            # scoreExceeded45Date
            # scoreExceeded75Date
            # scoreExceeded125Date
            # scoreExceeded200Date
            bannedUserIds
            commentsLocked
            # organizers
            organizerIds
            # group
            groupId
            eventType
            isEvent
            # reviewedByUser
            reviewedByUserId
            reviewForCuratedUserId
            startTime
            localStartTime
            endTime
            localEndTime
            eventRegistrationLink
            joinEventLink
            onlineEvent
            globalEvent
            mongoLocation
            googleLocation
            location
            contactInfo
            facebookLink
            meetupLink
            website
            eventImageId
            types
            metaSticky
            sharingSettings
            shareWithUsers
            linkSharingKey
            linkSharingKeyUsedBy
            commentSortOrder
            hideAuthor
            tableOfContents
            # tableOfContentsRevision(version)
            showModerationGuidelines
            moderationStyle
            hideCommentKarma
            commentCount
            # recentComments(
            # commentsLimit
            # maxAgeHours
            af
            # contents(version)
            # revisions(limit = 5)
            version
            pingbacks
            # moderationGuidelines(version)
            # moderationGuidelinesRevisions(limit = 5)
            moderationGuidelinesVersion
            # customHighlight(version)
            # customHighlightRevisions(limit = 5)
            customHighlightVersion
            af
            afDate
            afBaseScore
            afExtendedScore
            afCommentCount
            afLastCommentedAt
            afSticky
            # suggestForAlignmentUsers
            suggestForAlignmentUserIds
            reviewForAlignmentUserId
        }}
      }}
    }}
"""

def get_full_schema(limit, offset=0):
    return POST_FULL_SCHEMA.format(limit=limit, offset=offset)