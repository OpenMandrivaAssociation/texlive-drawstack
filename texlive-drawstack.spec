# revision 19627
# category Package
# catalog-ctan /macros/latex/contrib/drawstack
# catalog-date 2010-08-23 11:19:04 +0200
# catalog-license lppl1.3
# catalog-version undef
Name:		texlive-drawstack
Version:	20100823
Release:	2
Summary:	Draw execution stacks
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/drawstack
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/drawstack.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/drawstack.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This simple LaTeX package provides support for drawing
execution stack (typically to illustrate assembly language
notions). The code is written on top of TikZ.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/drawstack/drawstack.sty
%doc %{_texmfdistdir}/doc/latex/drawstack/README
%doc %{_texmfdistdir}/doc/latex/drawstack/stack-example.pdf
%doc %{_texmfdistdir}/doc/latex/drawstack/stack-example.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 20100823-2
+ Revision: 751091
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20100823-1
+ Revision: 718262
- texlive-drawstack
- texlive-drawstack
- texlive-drawstack
- texlive-drawstack

