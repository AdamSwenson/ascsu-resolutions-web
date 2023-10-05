from ResolutionManager.Repositories.ResolutionTemplateRespository import ResolutionTemplateRepository


def main(plenary, resolution):
    template_repo = ResolutionTemplateRepository(plenary=plenary)

    resolution = template_repo.create_file_from_template(resolution=resolution)
    template_repo.update_title(resolution)
    template_repo.update_header(resolution)


    print(resolution.__dict__)

    # resolution_name = "Opposing the existence of the CO"
    # resolution_number = 3456
    # committee = Committee('Faculty Affairs', 'FA')
    # cosponsors = [ Committee('Academic Affairs', 'AA')]
    # resolution = Resolution(resolution_number, resolution_name, committee, cosponsors)
    #
    # plenary = Plenary(year=2023,
    #                   month='September',
    #                   thursday_date=12,
    #                   friday_date=14,
    #                   first_reading_folder_id='1sv_4BUV5fk6Kcjss8HeSCJWnsLZJVpKC'
    #                   )


if __name__ == '__main__':
    main()
