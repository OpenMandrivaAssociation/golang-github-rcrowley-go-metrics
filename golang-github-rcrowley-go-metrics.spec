# http://github.com/rcrowley/go-metrics
%global goipath         github.com/rcrowley/go-metrics
%global commit          3113b8401b8a98917cde58f8bbd42a1b1c03b1fd

%gometa

Name:           golang-github-rcrowley-go-metrics
Version:        0
Release:        0.16%{?dist}
Summary:        Go port of Coda Hales Metrics library
License:        BSD
URL:            %{gourl}
Source0:        %{gosource}
Source1:        glide.yaml
Source2:        glide.lock

%description
Go port of Coda Hales Metrics library

%package devel
Summary:       %{summary}
BuildArch:     noarch

BuildRequires: golang(github.com/stathat/go)

%description devel
%{summary}

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.

%prep
%forgesetup
cp %{SOURCE1} %{SOURCE2} .

%install
%goinstall glide.lock glide.yaml

%check
# https://github.com/rcrowley/go-metrics/issues/249
%ifnarch %{power64} aarch64 s390x
%gochecks
%endif

%files devel -f devel.file-list
%license LICENSE
%doc memory.md README.md

%changelog
* Mon Oct 29 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.16.20181029git3113b84
- Bump to commit 3113b8401b8a98917cde58f8bbd42a1b1c03b1fd

* Tue Oct 23 2018 Nicolas Mailhot <nim@fedoraproject.org> - 0-0.15.gitdee209f
- redhat-rpm-config-123 triggers bugs in gosetup, remove it from Go spec files as it’s just an alias
- https://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/message/RWD5YATAYAFWKIDZBB7EB6N5DAO4ZKFM/

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.14.gitdee209f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jan Chaloupka <jchaloup@redhat.com> - 0-0.13.gitdee209f
- Upload glide files

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.12.gitdee209f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.11.gitdee209f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.10.gitdee209f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.9.gitdee209f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jul 21 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.8.gitdee209f
- https://fedoraproject.org/wiki/Changes/golang1.7

* Mon Feb 22 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.7.gitdee209f
- https://fedoraproject.org/wiki/Changes/golang1.6

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.6.gitdee209f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Aug 17 2015 jchaloup <jchaloup@redhat.com> - 0-0.5.gitdee209f
- Remove superfluous Provides
  related: #1250501

* Mon Aug 10 2015 Fridolin Pokorny <fpokorny@redhat.com> - 0-0.4.gitdee209f
- Update spec file to spec-2.0
- Disabled check due to test failure
  resolves: #1250501

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.3.gitdee209f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jan 12 2015 jchaloup <jchaloup@redhat.com> - 0-0.2.gitdee209f
- Bump to dee209f2455f101a5e4e593dea94872d2c62d85d
  adding missing provides
  related: #1120867

* Fri Sep 19 2014 Lokesh Mandvekar <lsm5@fedoraproject.org> - 0-0.1.git3be59ce
- BuildArch: noarch for main package
- defattr and attrs aren't needed in files listing
- replacing repo and project values with macros

* Thu Jul 17 2014 Colin Walters <walters@verbum.org> 0-0.0.git3be59ce
- Initial package
